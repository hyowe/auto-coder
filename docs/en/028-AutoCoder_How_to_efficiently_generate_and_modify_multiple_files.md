# 028-AutoCoder_How to efficiently generate and modify multiple files

The tokens generated by our large model at one time are limited, and generally much smaller than the input. This means that if you need to generate a large amount of code, you may need to generate it in multiple rounds.

AutoCoder provides a great feature to help you efficiently generate and modify multiple files. You can achieve this by following these steps:

```yml
## When generating code, a file is generated each time. Now, large models cannot generate too many files at once, so multiple rounds of generation are needed
enable_multi_round_generate: true
```

There are two scenarios here,

## If you have enabled human_as_model

That is:

```yml
human_as_model: true
```
Then AutoCoder will pause during the code generation phase of the large model and put the prompt in the `target_file`. You need to copy and paste it to the web end, then copy all corresponding content (not just the code) to the AutoCoder command line, press Enter after typing `EOF`. At this point, AutoCoder will continue to give you a new prompt (usually the word `continue`), and then you continue to copy and paste it to the web end, copy the corresponding content to the AutoCoder command line, press Enter after typing `EOF`. Repeat this process until all your files are generated or the web end tells you that all files have been generated. At this point, you need to:

1. Press Enter after typing '\_\_complete\_\_'
2. Press Enter after typing `EOF`

This completes the final input process.

'\_\_complete\_\_' means you can end the multi-round conversation. `EOF` means end the current round and continue to the next round.

## If you have not enabled human_as_model

Then all operations will be automatically completed by AutoCoder. However, if your model cannot end accurately (for example, according to AutoCoder's requirements, giving '\_\_complete\_\_' at the end), it may enter an infinite loop. Fortunately, AutoCoder limits the maximum number of rounds to 10. If it exceeds 10 rounds, AutoCoder will automatically end.