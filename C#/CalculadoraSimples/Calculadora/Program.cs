
// Console.WriteLine("Bem vindo a calculadora simples!");

using System.Reflection.Metadata;

void ColocarAsterisco(string frase){
    int qtd_letra = frase.Length;
    string astericos = new String('*',qtd_letra); 
    Console.WriteLine(astericos) ;
};



void MensagemErro(string mensagem){
    Console.WriteLine(mensagem);
    Console.WriteLine("Pressione Enter para sair...");
    Console.ReadLine();
    Environment.Exit(0);

};


string FraseDeBoasVindas = "Bem vindo a calculadora simples!"; 
ColocarAsterisco(FraseDeBoasVindas);
Console.WriteLine(FraseDeBoasVindas);
ColocarAsterisco(FraseDeBoasVindas);

Console.WriteLine( 
    """
    1 - Somar ;
    2 - Subtrair ;
    3 - Dividir ; 
    4 - Multiplicar ;
    """
);

ColocarAsterisco("Realize a sua escolha de calculo : ");
Console.Write("Realize a sua escolha de calculo : ");
string input = Console.ReadLine();
int Opcao;
Console.WriteLine();
ColocarAsterisco("Realize a sua escolha de calculo : ");


if (!int.TryParse(input, out Opcao)){
    MensagemErro("A entrada digitada não é valida !!");
}else if (Opcao < 1 || Opcao > 4){
    MensagemErro("Digite um numero dentro do limite estabelecido  !!");
}


Console.Write("Informe o primeiro numero : ");
string PrimeiroNumero = Console.ReadLine();
float primeiro_ ;
Console.Write("Informe o segundo numero : ");
string SegundoNumero = Console.ReadLine();
float segundo_ ;
ColocarAsterisco("Informe o segundo numero : ");


if (!float.TryParse(PrimeiroNumero, out primeiro_)  ){
    MensagemErro("O primeiro  numero  digitado não esta no formato correto !!");
}

if (!float.TryParse(SegundoNumero, out segundo_)  ){
    MensagemErro("O segundo numero  digitado não esta no formato correto !!");
}


switch(Opcao)
{
    case 1:
    Console.WriteLine($"A soma dos numeros {primeiro_} e {segundo_} é : {primeiro_ + segundo_:F2}\n");
    break;
    case 2:
    Console.WriteLine($"A Subtração  dos numeros {primeiro_} e {segundo_} é : {primeiro_ - segundo_:F2}\n");
    break;
    case 3:
    Console.WriteLine($"A divisão dos numeros {primeiro_} e {segundo_} é : {primeiro_ / segundo_:F2}\n");
    break;
    case 4:
    Console.WriteLine($"A multiplicação  dos numeros {primeiro_} e {segundo_} é : {primeiro_ * segundo_:F2}\n");
    break;

    default:
    Console.WriteLine("Opção invalida !!");
    break;
}

