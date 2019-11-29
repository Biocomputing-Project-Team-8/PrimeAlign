import decimal

log2 = decimal.getcontext().log10(2)
log3 = decimal.getcontext().log10(3)
log5 = decimal.getcontext().log10(5)
log7 = decimal.getcontext().log10(7)


class Node:
    positive = True
    A = decimal.Decimal(0)
    C = decimal.Decimal(0)
    G = decimal.Decimal(0)
    T = decimal.Decimal(0)

    def __lt__(self, other):
        return self.A + self.C + self.G + self.T < other.A + other.C + other.G + other.T

    def __add__(self, other):
        node = Node()
        node.A = self.A + other.A
        node.C = self.C + other.C
        node.G = self.G + other.G
        node.T = self.T + other.T
        if other < self:
            node.positive = False
        return node

    def __eq__(self, other):
        return self.positive == other.positive and self.A == other.A and self.C == other.C and self.G == other.G and \
               self.T == other.T


class Sequence:
    sequence = None
    name = None
    length = None
    graph = None

    def __init__(self, sequence):
        self.sequence = sequence
        self.length = len(sequence)
        monomers = []
        for nucleotide in sequence:
            node = Node()
            if nucleotide == 'A':
                node.A = log2
            elif nucleotide == 'C':
                node.C = log3
            elif nucleotide == 'G':
                node.G = log5
            elif nucleotide == 'T':
                node.T = log7
            monomers.append(node)
        self.graph = []
        self.graph.insert(0, monomers)
        for i in range(1, self.length):
            k_mers = []
            for j in range(0, self.length - i):
                k_mers.append(self.graph[0][j] + self.graph[0][j + 1])
            self.graph.insert(0, k_mers)

    def global_alignment(self, other):
        graph_self = self.graph
        graph_other = other.graph
        if self.length > other.length:
            graph_self = self.graph[self.length - other.length:self.length]
        elif other.length > self.length:
            graph_other = other.graph[other.length - self.length:other.length]
        matches_self = []
        matches_other = []
        for i in range(0, len(graph_self)):
            range_matches = []
            range_k = []
            for j in range(0, len(matches_self)):
                range_matches.append([matches_self[j][0], i - matches_self[j][1] + 1 + matches_self[j][0]])
            start = 0
            for j in range(0, len(range_matches)):
                range_k.append([start, range_matches[j][0]])
                start = range_matches[j][1]
            range_k.append([start, len(graph_self[i])])
            range_matches = []
            range_m = []
            for j in range(0, len(matches_other)):
                range_matches.append([matches_other[j][0], i - matches_other[j][1] + 1 + matches_other[j][0]])
            start = 0
            for j in range(0, len(range_matches)):
                range_m.append([start, range_matches[j][0]])
                start = range_matches[j][1]
            range_m.append([start, len(graph_other[i])])
            for j in range(0, len(range_k)):
                offset = range_m[j][0]
                for k in range(range_k[j][0], range_k[j][1]):
                    for m in range(offset, range_m[j][1]):
                        if graph_self[i][k] == graph_other[i][m]:
                            matches_self.append([k, i])
                            matches_other.append([m, i])
                            offset = m + 1
                            break
            matches_self.sort()
            matches_other.sort()
        distance = []
        gap_self = []
        gap_other = []
        for i in range(0, len(matches_self)):
            distance.append(matches_other[i][0] - matches_self[i][0])
        for i in range(0, len(distance)):
            if distance[i] > 0:
                gap_self.append(distance[i])
                gap_other.append(0)
            elif distance[i] < 0:
                gap_self.append(0)
                gap_other.append(distance[i] * -1)
            else:
                gap_self.append(0)
                gap_other.append(0)
            for j in range(i + 1, len(distance)):
                distance[j] -= distance[i]
        aligned_sequence_self = ""
        start = 0
        for i in range(0, len(gap_self)):
            aligned_sequence_self += self.sequence[start:matches_self[i][0]]
            aligned_sequence_self += "-" * gap_self[i]
            start = matches_self[i][0]
        aligned_sequence_self += self.sequence[start:self.length]
        aligned_sequence_other = ""
        start = 0
        for i in range(0, len(gap_other)):
            aligned_sequence_other += other.sequence[start:matches_other[i][0]]
            aligned_sequence_other += "-" * gap_other[i]
            start = matches_other[i][0]
        aligned_sequence_other += other.sequence[start:other.length]
        if len(aligned_sequence_self) > len(aligned_sequence_other):
            aligned_sequence_other += "-" * (len(aligned_sequence_self) - len(aligned_sequence_other))
        elif len(aligned_sequence_other) > len(aligned_sequence_self):
            aligned_sequence_self += "-" * (len(aligned_sequence_other) - len(aligned_sequence_self))
        return aligned_sequence_self, aligned_sequence_other


sequence1 = Sequence(
    "TCTGTAGACCAACAGAACTGTCACAGCTTTATTTTGTGACTCATTATATTACAACATAGAAATATGCATTTTAATACTTCATATAAAGTTATTGACATACAAAATTTTTTTTC")
sequence2 = Sequence(
    "TGTGTAGACCAGCAGGACTGTCACAGCTTTATTTTGTGACTCATAACATAGAAACAAGCTTTTAAAAAAACACGTCATATAAAGTTATTCACAATACAATTTTTTTCAGTT")
alignment = sequence1.global_alignment(sequence2)
print(alignment[0])
print(alignment[1])
