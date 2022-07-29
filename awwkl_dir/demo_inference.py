import os
import subprocess

# 4 videos in MOT20 test set, use the first 250 frames of each video (10 seconds)
# for folder_name in ['MOT20-04', 'MOT20-06', 'MOT20-07', 'MOT20-08']:
#     command = f'python demo/demo_mot_vis.py configs/mot/deepsort/deepsort_faster-rcnn_fpn_4e_mot17-private-half.py --input awwkl_dir/awwkl_data/mot20/{folder_name} --fps 25 --output awwkl_dir/awwkl_results/deepsort/mot20_segment_{folder_name}.mp4'

#     subprocess.call(command)

#     command = f'python demo/demo_mot_vis.py configs/mot/bytetrack/bytetrack_yolox_x_crowdhuman_mot17-private-half.py --input awwkl_dir/awwkl_data/mot20/{folder_name} --fps 25 --output awwkl_dir/awwkl_results/bytetrack/mot20_segment_{folder_name}.mp4 --checkpoint awwkl_dir/awwkl_models/bytetrack_yolox_x_crowdhuman_mot17-private-half_20211218_205500-1985c9f0.pth'

#     subprocess.call(command)

# 4 videos in MOT20 test set, use the first 250 frames of each video (10 seconds)
# for folder_name in ['MOT17-02']:
#     command = f'python demo/demo_mot_vis.py configs/mot/deepsort/deepsort_faster-rcnn_fpn_4e_mot17-private-half.py --input awwkl_dir/awwkl_data/mot17-val/{folder_name} --fps 30 --output awwkl_dir/awwkl_results/deepsort/mot17-val_segment_{folder_name}.mp4'

#     subprocess.call(command)

#     command = f'python demo/demo_mot_vis.py configs/mot/bytetrack/bytetrack_yolox_x_crowdhuman_mot17-private-half.py --input awwkl_dir/awwkl_data/mot17-val/{folder_name} --fps 30 --output awwkl_dir/awwkl_results/bytetrack/mot17-val_segment_{folder_name}.mp4 --checkpoint awwkl_dir/awwkl_models/bytetrack_yolox_x_crowdhuman_mot17-private-half_20211218_205500-1985c9f0.pth'

#     subprocess.call(command)

for folder_name in ['MOT17-04']:
    # command = f'python demo/demo_mot_vis.py configs/mot/deepsort/deepsort_faster-rcnn_fpn_4e_mot17-private-half.py --input awwkl_dir/awwkl_data/mot17-val/{folder_name} --fps 30 --output awwkl_dir/awwkl_results/deepsort/mot17-val_full_{folder_name}.mp4'

    # subprocess.call(command)

    command = f'python demo/demo_mot_vis.py configs/mot/bytetrack/bytetrack_yolox_x_crowdhuman_mot17-private-half.py --input awwkl_dir/awwkl_data/mot17-val/{folder_name} --fps 30 --output awwkl_dir/awwkl_results/bytetrack/mot17-val_full_{folder_name}.mp4 --checkpoint awwkl_dir/awwkl_models/bytetrack_yolox_x_crowdhuman_mot17-private-half_20211218_205500-1985c9f0.pth'

    subprocess.call(command)
