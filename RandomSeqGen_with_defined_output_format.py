import argparse
import random

def random_sequence_generator(number_of_sequences=None, length_of_sequence=None):
    DNA_nucleotides = ["G", "C", "A", "T"]
    random_seq_lst = []
    if number_of_sequences is not None and length_of_sequence is not None:
        for i in range(number_of_sequences):
            random_seq = random.choices(DNA_nucleotides, weights=[1, 1, 1, 1], k=length_of_sequence)
            random_seq_lst.append(random_seq)
        return random_seq_lst

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
