# VARIANT 1
#
 print("""
               *     *      * * *  *   *
              * *    *      *       * *
             *   *   *      * * *    *
            * * * *  *   *  *       * *
           *       * * * *  * * *  *   *
       """)

# VARIANT 2 - the following code is working good in Terminal only
#
 from art import *
 art_name = text2art("ALEXANDER", font="caligraphy")
 print(art_name)


 print('''
 \\a     Bell (alert)
 \\b     Backspace
 \\n     New line
 \\t     Horizontal tab
 \\\     Backslash \\
 \\”     Double quotation mark“
 \\’     Single quotation mark‘
       ''')


 Number1 = int(input("please insert Number 1: "))
 Number2 = int(input("please insert Number 2: "))
 print("Number 1 + Number 2 =", Number1 + Number2)
 print("Number 1 // Number 2 =", Number1 // Number2)
 print("Number 1 % Number 2 =", Number1 % Number2)
 print("Number 1 ** Number 2 =", Number1 ** Number2)

