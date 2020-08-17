class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        dim = len(matrix)
        for i in range(dim):
            for j in range(i,dim):
                # transpose
                matrix[j][i],matrix[i][j] = matrix[i][j],matrix[j][i]
        for i in range(dim):
            matrix[i].reverse()
    
def main():
    input_matrix = [
                    [ 5, 1, 9,11],
                    [ 2, 4, 8,10],
                    [13, 3, 6, 7],
                    [15,14,12,16]
                    ]
    s= Solution()
    s.rotate(input_matrix)
    print(input_matrix)
    

if __name__ == "__main__":
    main()