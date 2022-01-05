#!/bin/bash

export CUDA_VISIBLE_DEVICES=0,1,2,3
#export HF_HOME=/home/yanyang20/gsl/cache
export HF_HOME=/export/App/training_platform/PinoModel/cache
# tgt_domains: AddToPlaylist BookRestaurant GetWeather PlayMusic RateBook SearchCreativeWork SearchScreeningEvent atis

for tgt_domain in AddToPlaylist BookRestaurant GetWeather PlayMusic RateBook SearchCreativeWork SearchScreeningEvent atis; do
  for shot_num in 0 20 50; do
    python3 main.py $tgt_domain \
      --model-name t5-large \
      --batch-size 16 \
      --num-epochs 100 \
      --lr 2e-5 \
      --query-max-seq-length 128 \
      --response-max-seq-length 64 \
      --num-beams 2 \
      --query-schema description \
      --response-schema plain \
      --shot-num $shot_num \
      --patience 5
  done
done

