// 2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
// Какое самое маленькое число делится нацело на все числа от 1 до 20?

#include <stdio.h>
#include <stdlib.h>

unsigned long long factorial(int n) {
  unsigned long long t = 1;
  for (int i = 2; i <= n; i++) t *= i;
  return t;
}

int is_prime(unsigned long long n) {
  if (!(n & 1)) return 0;
  unsigned long long d = 3;
  while (d * d <= n) {
    if (n % d == 0) return 0;
    d += 2;
  }
  return 1;
}

int main (int argc, char *argv[]) {
  unsigned int *arr = (unsigned int) malloc(1*sizeof(unsigned int));
  printf("%llu", factorial(20));
}