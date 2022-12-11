# Random Tiling as a Form of Data Augmentation on Short Interval Speech Events
- [AudioMAE](https://github.com/facebookresearch/AudioMAE) is a relatively new pretraining method for audio classification tasks built on the ViT backbone.
- [CSLT-TRIVIAL-I](https://github.com/CSLT-THU/ICASSP2018-trivial/tree/master/CSLT-TRIVIAL-I) is a dataset composing of 75 speakers uttering short interval speech events such as laughing and coughing. It is designed to perform speaker recognition tasks.
- This repo uses the same method as AudioMAE to finetune the model for speaker identification using laughing and coughing data from CSLT-TRIVIAL-I. Several data augmentation methods are used, among which random tiling is the best.

## Steps to reproduce the experiments
1. Download the finetuned model checkpoint from [AudioMAE](https://github.com/facebookresearch/AudioMAE) repo, place it under `./ckpt/`.
2. Download the [CSLT-TRIVIAL-I](https://github.com/CSLT-THU/ICASSP2018-trivial/tree/master/CSLT-TRIVIAL-I) dataset (specifically, the `laugh` and `cough` folder), place them under `./data/ICASSP2018-trivial/`.
3. Run data preparation and augmentation scripts:
```
python gen_class_labels.py
python tile_wavs.py
python gen_train_eval.py
```
4. Finetune and evaluate the model following the launch settings in `./.vscode/launch.json` (need to install VSCode).

## Results
Speaker recognition (laughing):
Method | Acc.(%)
------ | ------
Pading | 72.6
Tiling | 72.6
Rand. Tiling | **75.5**

Speaker recognition (coughing):
Method | Acc.(%)
------ | ------
Pading | 85.8
Tiling | 86.8
Rand. Tiling | **89.2**
