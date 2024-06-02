import byzerllm
from typing import Optional
from autocoder.common import AutoCoderArgs
from autocoder.common.code_auto_merge import CodeAutoMerge
from autocoder.common.code_auto_merge_diff import CodeAutoMergeDiff
from autocoder.common.code_auto_merge_strict_diff import CodeAutoMergeStrictDiff
from autocoder.common.code_auto_merge_editblock import CodeAutoMergeEditBlock
from autocoder.common.code_auto_generate import CodeAutoGenerate
from autocoder.common.code_auto_generate_diff import CodeAutoGenerateDiff
from autocoder.common.code_auto_generate_strict_diff import CodeAutoGenerateStrictDiff
from autocoder.common.code_auto_generate_editblock import CodeAutoGenerateEditBlock
from autocoder.index.index import build_index_and_filter_files
from autocoder.regexproject import RegexProject
from loguru import logger


class ActionRegexProject:
    def __init__(
        self, args: AutoCoderArgs, llm: Optional[byzerllm.ByzerLLM] = None
    ) -> None:
        self.args = args
        self.llm = llm
        self.pp = None

    def run(self):
        args = self.args
        if not args.project_type.startswith(
            "human://"
        ) and not args.project_type.startswith("regex://"):
            return False

        args = self.args
        pp = RegexProject(args=args, llm=self.llm)
        self.pp = pp
        pp.run()
        source_code = pp.output()
        if self.llm:
            source_code = build_index_and_filter_files(
                llm=self.llm, args=args, sources=pp.sources
            )
        self.process_content(source_code)

    def process_content(self, content: str):
        args = self.args

        if args.execute and self.llm and not args.human_as_model:
            if len(content) > self.args.model_max_input_length:
                logger.warning(
                    f"Content length is {len(content)}, which is larger than the maximum input length {self.args.model_max_input_length}. chunk it..."
                )
                content = content[: self.args.model_max_input_length]

        if args.execute:
            if args.auto_merge == "diff":
                generate = CodeAutoGenerateDiff(
                    llm=self.llm, args=self.args, action=self
                )
            elif args.auto_merge == "strict_diff":
                generate = CodeAutoGenerateStrictDiff(
                    llm=self.llm, args=self.args, action=self
                )
            elif args.auto_merge == "editblock":
                generate = CodeAutoGenerateEditBlock(
                    llm=self.llm, args=self.args, action=self
                )
            else:
                generate = CodeAutoGenerate(llm=self.llm, args=self.args, action=self)
            if self.args.enable_multi_round_generate:
                result, _ = generate.multi_round_run(
                    query=args.query, source_content=content
                )
            else:
                result, _ = generate.single_round_run(
                    query=args.query, source_content=content
                )
            content = "\n\n".join(result)

        with open(args.target_file, "w") as file:
            file.write(content)

        if args.execute and args.auto_merge:
            logger.info("Auto merge the code...")
            if args.auto_merge == "diff":
                code_merge = CodeAutoMergeDiff(llm=self.llm, args=self.args)
                code_merge.merge_code(content=content)
            elif args.auto_merge == "strict_diff":
                code_merge = CodeAutoMergeStrictDiff(llm=self.llm, args=self.args)
                code_merge.merge_code(content=content)
            elif args.auto_merge == "editblock":
                code_merge = CodeAutoMergeEditBlock(llm=self.llm, args=self.args)
                code_merge.merge_code(content=content)
            else:
                code_merge = CodeAutoMerge(llm=self.llm, args=self.args)
                code_merge.merge_code(content=content)
