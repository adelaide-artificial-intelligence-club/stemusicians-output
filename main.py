
import os, tensorflow, magenta
from magenta import music
from magenta.protobuf import music_pb2
from magenta.models.music_vae import configs
from magenta.models.music_vae.trained_model import TrainedModel

def main():
    # load trained model
    music_vae = TrainedModel(
        configs.CONFIG_MAP['cat-mel_2bar_big'],
        batch_size=4,
        checkpoint_dir_or_path='checkpoints/mel_2bar_big.ckpt')

    # generate some sequences
    generated_sequences = music_vae.sample(n=10, length=80, temperature=1.0)

    # save sequences to files
    for n, sequence in enumerate(generated_sequences):
        music.sequence_proto_to_midi_file(sequence,
            os.path.join('output', str(n) + '.mid'))

if __name__ == '__main__':
    main()
