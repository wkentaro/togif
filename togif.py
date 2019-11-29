import argparse
import os.path as osp

import imageio
import imgviz
import tqdm


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument('input_file', help='input video')
    parser.add_argument('--fps', type=float, default=1, help='fps')
    parser.add_argument('--speed', type=float, default=1, help='speed')
    parser.add_argument('--start', type=float, default=0, help='start')
    parser.add_argument('--duration', type=float, help='duration')
    parser.add_argument('--resize', type=float, default=1, help='resize')
    args = parser.parse_args()

    output_file = osp.splitext(args.input_file)[0] + '.gif'

    reader = imageio.get_reader(args.input_file)
    meta = reader.get_meta_data()
    fps_src = meta['fps']

    width, height = None, None
    if args.resize:
        width, height = meta['size']
        width = int(round(args.resize * width))
        height = int(round(args.resize * height))

    if args.fps is None:
        args.fps = fps_src

    writer = imageio.get_writer(output_file, fps=args.fps * args.speed)

    scale = 1. * args.fps / fps_src

    j = -1
    for i in tqdm.trange(reader.get_length()):
        elapsed_time = i * 1. / meta['fps']
        if elapsed_time < args.start:
            continue

        frame = reader.get_data(i)
        if width is not None and height is not None:
            frame = imgviz.resize(
                frame, height=height, width=width, interpolation='linear'
            )

        j_detail = i * scale
        if int(round(j_detail)) != j:
            writer.append_data(frame)
            j = int(round(j_detail))

        if args.duration:
            duration = elapsed_time - args.start
            if duration >= args.duration:
                break

    reader.close()
