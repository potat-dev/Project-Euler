// Простые делители числа 13195 - это 5, 7, 13 и 29.
// Каков самый большой делитель числа 600851475143, являющийся простым числом?

#include <stdio.h>
#include <stdlib.h>

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
  unsigned long long n = 600851475143;
  unsigned long long i, max = 0, t = 0;

  for (i = 1; i*i < n; i++) {
    if (n % i == 0) {
      t = n / i;
      if (is_prime(i) && i > max) max = i;
      if (is_prime(t) && t > max) max = t;
    }
  }
  printf("%llu", max);
}