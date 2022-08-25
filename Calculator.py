# Matrix Calculator Assignment
import time
print('Matrix Calculator')
while True:
    time.sleep(0.5)
    print('\nOPERATIONS MENU:\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Transpose\n5.Identity Matrix\n6.Exit\n ')
    n=int(input('select an operation from menu:'))
    if n==1:
        print('ADDITION')
        row=int(input("Entre row's number of matrix:"))
        col=int(input("Entre column's number of matrix:"))
        print('Entre values for MATRIX_1:')
        mat1=[[int(input("enter value in cell["+str(j+1)+"]["+str(i+1)+"]:"))for i in range(col)] for j in range(row)]
        print('MATRIX_1')
        for i in range(row):
            for j in range(col):
                print(mat1[i][j],end='\t')
            print()

        print('Entre values for MATRIX_2:')
        mat2=[[int(input("enter value in cell["+str(j+1)+"]["+str(i+1)+"]:"))for i in range(col)] for j in range(row)]
        print('MATRIX_2')
        for i in range(row):
            for j in range(col):
                print(mat2[i][j],end='\t')
            print()

        result=[[0 for i in range(col)]for j in range(row)]
        for i in range(len(mat1)): #row
            for j in range(len(mat1[0])): #column
                result[i][j]=mat1[i][j]+mat2[i][j]
        print('result of MATRIX is:')
        for i in range(row):
            for j in range(col):
                print(result[i][j],end='\t')
            print()
    elif n==2:
        print('SUBTRACTION')
        row=int(input("Entre row's number of matrix:"))
        col=int(input("Entre column's number of matrix:"))
        
        print('Entre values for MATRIX_1:')
        mat1=[[int(input("enter value in cell["+str(j+1)+"]["+str(i+1)+"]:"))for i in range(col)] for j in range(row)]
        print('MATRIX_1')
        for i in range(row):
            for j in range(col):
                print(mat1[i][j],end='\t')
            print()

        print('Entre values for MATRIX_2:')
        mat2=[[int(input("enter value in cell["+str(j+1)+"]["+str(i+1)+"]:"))for i in range(col)] for j in range(row)]
        print('MATRIX_2')
        for i in range(row):
            for j in range(col):
                print(mat2[i][j],end='\t')
            print()

        result=[[0 for i in range(col)]for j in range(row)]
        for i in range(len(mat1)): #row
            for j in range(len(mat1[0])): #column
                result[i][j]=(mat1[i][j]) - (mat2[i][j])
        print('result of MATRIX is:')
        for i in range(row):
            for j in range(col):
                print(result[i][j],end='\t')
            print()
    elif n==3:
        print('MULTIPLICATION')
        p=int(input("Entre row's number of MATRIX_1:"))
        q=int(input("Entre column's number of MATRIX_2:"))
        h=int(input("Entre row's no. of MATRIX_2/column no. of MATRIX_1:"))
        
        print('Entre values for MATRIX_1:')
        mat1=[[int(input("enter value in cell["+str(j+1)+"]["+str(i+1)+"]:"))for i in range(h)] for j in range(p)]
        print('MATRIX_1')
        for i in range(p):
            for j in range(h):
                print(mat1[i][j],end='\t')
            print()

        print('Entre values for MATRIX_2:')
        mat2=[[int(input("enter value in cell["+str(j+1)+"]["+str(i+1)+"]:"))for i in range(q)] for j in range(h)]
        print('MATRIX_2')
        for i in range(h):
            for j in range(q):
                print(mat2[i][j],end='\t')
            print()

        result=[[0 for i in range(q)]for j in range(p)]
        for i in range(p):
            for j in range(q):
                for k in range(h):
                    result[i][j]= result[i][j] + mat1[i][k] * mat2[k][j]

        print('result of MATRIX is:')
        for i in range(p):
            for j in range(q):
                print(result[i][j],end='\t')
            print()
    elif n==4:
        print('TRANSPOSE')
        row=int(input("Entre row's number of matrix:"))
        col=int(input("Entre column's number of matrix:"))
        
        print('Entre value of MATRIX:')
        mat1=[[int(input("enter value in cell["+str(j+1)+"]["+str(i+1)+"]:"))for i in range(col)] for j in range(row)]
        print('MATRIX')
        for i in range(row):
            for j in range(col):
                print(mat1[i][j],end='\t')
            print()
            
        result=[[0 for i in range(row)]for j in range(col)]
        for i in range(col):
            for j in range(row):
                result[i][j]=mat1[j][i]
        print('TRANSPOSE')
        for i in range(col):
            for j in range(row):
                print(result[i][j],end='\t')
            print()
    elif n==5:
        print('IDENTITY')
        order=int(input('Entre number for order of Identity matrix:'))
        for i in range(order):
            for j in range(order):
                if i==j:
                    print(format('1','<5'),end='')
                else:
                    print(format('0','<5'),end='')
            print()
    else:
        break
print('End of calculations')
