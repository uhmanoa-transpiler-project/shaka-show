#include <stdio.h>
#include <fstream>

int main() {
	std:: ofstream ofs ("Test.cpp", std::ofstream::out);
	ofs << "lorem ipsum";
	ofs.close();

	return 0;
}
