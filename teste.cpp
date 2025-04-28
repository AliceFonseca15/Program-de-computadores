#include <iostream>
long long soma(long long a, long long b) {
    return a + b;
}
int main() {
    long long a, b;
    std::cin >> a >> b;
    std::cout << soma(a, b) << std::endl;
    return 0;
}
