package com.company;

import java.util.Scanner;

public class Main {

    static void getBin(int number){
        if (number != 1){
            getBin(number >> 1);
        }
        System.out.print(number & 1);
    }

    static void replaceOneToZero(int number){
        System.out.println(number & (number - 1));
    }

    static void replaceZeroToOne(int number){
        System.out.println(number | (number + 1));
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        replaceZeroToOne(a);
    }
}
