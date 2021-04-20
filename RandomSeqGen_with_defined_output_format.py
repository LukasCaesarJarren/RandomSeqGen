import argparse
from RandomSeqGen_basic import random_sequence_generator


def write_random_sequences_in_file_with_format(random_seq_lst):
    with open('random_sequences_formatted.txt', 'w') as file:
        for index, seq in enumerate(random_seq_lst):
            name = '>' + str(index)
            sequence = ''.join(seq)
            file.write(name + '\n')
            file.write(sequence + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', type=int, metavar='number of generated seqs')
    parser.add_argument('-l', type=int, metavar='length of seqs')
    args = parser.parse_args()
    random_seqs = random_sequence_generator(number_of_sequences=args.n, length_of_sequence=args.l)
    write_random_sequences_in_file_with_format(random_seq_lst=random_seqs)
