public class RunLengthEncoding {
    // Exercise 3. a)
    public static String compress(String text) {
        StringBuilder compressedText = new StringBuilder();
        char[] charArrayOfText = text.toCharArray();

        int counter = 1;

        for (int i = 0; i < charArrayOfText.length; i++) {
            if (i + 1 < charArrayOfText.length && charArrayOfText[i] == charArrayOfText[i+1]) {
                counter++;
            } else {
                if (counter > 1) {
                    compressedText.append(counter + Character.toString(charArrayOfText[i]));
                } else {
                    compressedText.append(charArrayOfText[i]);
                }

                counter = 1;
            }

        }
        return compressedText.toString();
    }

    // Exercise 3. b)
    public static String decompress(String text) {
        StringBuilder compressedText = new StringBuilder();
        char[] charArrayOfText = text.toCharArray();

        int counter = 0;

        for (char currentChar : charArrayOfText) {
            if (Character.isDigit(currentChar)) {
                counter = counter * 10 + currentChar - '0';
            } else {
                if (counter == 0) {
                    counter = 1;
                }
                while (counter > 0) {
                    compressedText.append(currentChar);
                    counter--;
                }
            }

        }

        return compressedText.toString();
    }

    // Main
    public static void main(String[] args) {
        // String dna = "ACAAAGATGCCATTGTAA";
        String dna = "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGG"
                + "GCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCG"
                + "AGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCT"
                + "CCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGC"
                + "CGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGA"
                + "AGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAG"
                + "GAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCA"
                + "TGAATGCTCACGCAAGTTTAATTACAGACCTGTGA";

        String dnaCompressed = compress(dna);
        System.out.println(dnaCompressed + "\nlength: " + dnaCompressed.length() + '\n');

        String dnaDecompressed = decompress(dnaCompressed);
        System.out.println(dnaDecompressed + "\nlength: " + dnaDecompressed.length() + "\nequals? " + dna.equals(dnaDecompressed));
    }
}
