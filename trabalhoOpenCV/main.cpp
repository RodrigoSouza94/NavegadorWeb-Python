#include <iostream>
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

int main() {
    // 1. Carrega as duas imagens da pasta
    Mat img1 = imread("imagens/entrada.png");
    Mat img2 = imread("imagens/familia.png");

    // Valida se ambas foram encontradas
    if (img1.empty() || img2.empty()) {
        cout << "Erro ao carregar uma das imagens!" << endl;
        return 1;
    }

    // 2. Cria as variáveis de saída
    Mat cinza1, cinza2;

    // 3. Aplica a conversão em cada uma
    cvtColor(img1, cinza1, COLOR_BGR2GRAY);
    cvtColor(img2, cinza2, COLOR_BGR2GRAY);

    // 4. Salva as duas fotos na pasta de saídas
    imwrite("saidas/resultado_entrada.png", cinza1);
    imwrite("saidas/resultado_familia.png", cinza2);

    cout << "Sucesso! As duas fotos foram salvas em cinza." << endl;
    return 0
}