#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 14 21:54:54 2022

@author: gideon
"""
import time
import sys

def program():
    def main_page():
        print("WELCOME")
        print("1.Factorial \n2.Addition \n3.substraction \n4.Multiplication \n5.Permutation \n6.Combination \n\nTo Exit program press N")
        choice = str(input("choose an operator: "))
        while True:
            if choice == "1":
                facto()
            elif choice == "2":
                add()
            elif choice == "3":
                sub()
            elif choice == "4":
                Mult()
            elif choice == "5":
               perm()
            elif choice == "6":
                comb()
            elif choice == "N" or "n":
                print("THANKS FOR USING OUR PROGRAM, SEE YOU ANOTHER TIME")
                sys.exit()
                
    
    def facto():
        print("""FACTORIAL OPERATOR""")
        n = int(input("Enter a number: "))
        f=1
        for i in range(1,n+1):
            f=f*i
        print("Answer: ",f)
        print('\n')
        time.sleep(1),print("Do you want to use Factorial operator again? \nIf Yes enter Y")
        print('\n')
        print('press 0 to go to the Main menu')
        opt = str(input("Enter reply: "))
        if opt == "0":
            main_page()
        elif opt == "Y" or "y":
            facto()
    
    def add():
        print("""ADDITION OPERATOR""")
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        sum = num1 + num2
        print("Answers: ",sum)
        print('\n')
        time.sleep(1),print("Do you want to use Addition operator again? \nIf Yes enter Y")
        print('\n')
        print('press 0 to go to the Main menu')
        opt = str(input("Enter reply: "))
        if opt == "0":
            main_page()
        elif opt == "Y" or "y":
            add()
    def sub():
        print("""SUBTRACTION OPERATOR""")
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        minus = num1 - num2
        print("Answer: ",minus)
        print('\n')
        time.sleep(1),print("Do you want to use Substraction operator again? \nIf Yes enter Y")
        print('\n')
        print('press 0 to go to the Main menu')
        opt = str(input("Enter reply: "))
        if opt == "0":
            main_page()
        elif opt == "Y" or "y":
            sub()
        
    def Mult():
        print("""MULTIPLICATION OPERATOR""")
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        product = num1 * num2
        print("Answer: ",product)
        print('\n')
        time.sleep(1),print("Do you want to use Multiplication operator again? \nIf Yes enter Y")
        print('\n')
        print('press 0 to go to the Main menu')
        opt = str(input("Enter reply: "))
        if opt == "0":
            main_page()
        elif opt == "Y" or "y":
            Mult()
    
    def perm():
        def fact(n):
            f=1
            for i in range(1,n+1):
                f=f*i
            return f
        print("""PERMUTATION OPERATOR""")
        n = int(input("Enter N value: "))
        r = int(input("Enter R value: "))
        result = fact(n)//fact(n-r)
        print("Answer:",result)
        print('\n')
        time.sleep(1),print("Do you want to use Permutation operator again? \nIf Yes enter Y")
        print('\n')
        print('press 0 to go to the Main menu')
        opt = str(input("Enter reply: "))
        if opt == "0":
            main_page()
        elif opt == "Y" or "y":
            perm()
    
    def comb():
        def fact(n):
            f=1
            for i in range(1,n+1):
                f=f*i
            return f
        print("""COMBINATION OPERATOR""")
        n = int(input("Enter N value: "))
        r = int(input("Enter R value: "))
        nr = n-r
        n_facto = fact(n)
        r_facto = fact(r)
        nr_facto = fact(nr)
        rnr = r_facto*nr_facto
        combinate = n_facto//rnr
        print("Answer: ",combinate)
        print('\n')
        time.sleep(1),print("Do you want to use Combination operator again? \nIf Yes enter Y")
        print('\n')
        print('press 0 to go to the Main menu')
        opt = str(input("Enter reply: "))
        if opt == "0":
            main_page()
        elif opt == "Y" or "y":
            comb()
        
        
    main_page()
    
program()
    
