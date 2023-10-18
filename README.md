# LaunchpadGPT
This repo is for paper accepted by ICMC 2023: LaunchpadGPT: Language Model as Music Visualization Designer on Launchpad 

<img src="/framework.png"> 

### Quick Start

1. download the prompt-completion pairs' data `prompt_completion.txt` from [[here]](https://drive.google.com/file/d/1ZBQtDop9jGhcSjpZwWKHC-k6QK4pVNe-/view?usp=sharing), and put it in the `./data` folder. 

2. turn `prompt_completion.txt` from raw text into one large stream of integers:

```shell
python data/prompt_completion/prepare.py
```
This creates a `train.bin` and `val.bin` in the prompt_completion directory.

3. train a LaunchpadGPT:

```shell
python train.py config/train_launchpad_gpt.py
```

### Sampling

This is an example of generate RGB-X tuples (completion) given the MFCC features with 128 dims of input music (prompt):

```shell
python sample.py --out_dir=out-launchpad-gpt --start='{"prompt": [-29.44, 108.58, -15.65, 36.5, 2.3, 14.21, 4.92, 20.2, -2.59, 9.43, 10.56, 20.83, -0.24, 1.78, -12.75, 2.06, -4.75, 0.09, -4.64, -7.97, -0.51, -4.5, -3.58, -9.82, -1.73, 8.06, 1.05, -1.21, -1.25, -5.44, -9.97, -16.69, -5.6, 2.49, 0.04, 5.14, -0.37, -8.98, -5.22, -8.35, -14.0, 5.34, 3.24, -0.72, -4.3, -1.48, -3.27, 1.1, -2.93, -5.9, -3.68, 2.54, 5.99, 2.21, -6.68, 1.52, 0.23, 1.74, 1.14, -1.17, 1.01, -0.78, -5.34, -0.31, 1.09, 4.35, -0.25, -0.52, -0.14, -1.47, 9.78, 1.56, -1.56, 5.22, -1.96, -0.0, 1.63, 0.18, -0.63, 3.86, -1.81, 3.28, -0.89, 1.4, -0.75, -2.01, -0.78, 1.12, -0.02, 1.75, 0.24, -0.99, -1.75, 3.75, 1.06, 1.01, 2.99, 1.59, 3.54, -1.33, -3.71, 1.18, 1.11, -0.47, 0.76, -0.96, -1.03, 1.0, -0.48, -0.51, 0.9, 0.36, -0.4, 1.28, -0.78, 1.92, 0.57, 2.5, 1.79, 0.8, -0.5, -0.19, -2.1, -1.51, -0.57, -1.17, 0.08, 0.45], "completion":'
```

The generated Launchpad can be found in `./outputs/sample_outs`

### Inference

The `infer.py` can generate the Launchpads with validation data `val_prompts.json`.


```shell
python infer.py
```
The results will be saved in the `./outputs/val_outs`

### Evaluation

To evaluate the results, you can download the ground-truth data `gt_frame` from [[here]](https://drive.google.com/file/d/13UNtQgTKaUJomo3vxwBuUC7W25sRYqgz/view?usp=sharing) to `./outputs`.

Then run the script to calculate the scores:

```shell
python -m pytorch_fid outputs/gt_frames outputs/val_outs
```

The original Launchpad-playing video can be downloaded from [[here]](https://drive.google.com/file/d/1ikugWFBwkRm0V6AlDoRswdC3knrvLZCt/view?usp=sharing).

### Acknowledgement
The project is based on [NanoGPT](https://github.com/karpathy/nanoGPT), [midifox](http://midifox.com/). Thanks for the authors for their efforts.
