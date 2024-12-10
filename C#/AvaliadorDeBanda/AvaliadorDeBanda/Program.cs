// See https://aka.ms/new-console-template for more information

using System.Collections.ObjectModel;
using System.Linq.Expressions;
using System.Runtime.InteropServices;
using Microsoft.VisualBasic;


List<string> bandas = new List<string>(){
    "uclã",
    "Duzz",
    "The box",
    "Cypher"
};

string mensagemDeBoasVindas = "Bem Vindo ao Avaliador de Banda!!";
Console.WriteLine(mensagemDeBoasVindas);


void ExibirAsteriscos(string mensagem)
{
    string astericos = new string('*', mensagem.Length);
    Console.WriteLine(astericos);
}

void mensagemDeOpcao(string mensagemDeBoasVindas)
{
    ExibirAsteriscos(mensagemDeBoasVindas);
    Console.WriteLine(
        """
        1 - VISUALIZAR BANDAS 
        2 - CADASTRAR BANDA
        3 - CADASTRAR MUSICA
        4 - AVALIAR BANDA
        """
        );
    ExibirAsteriscos(mensagemDeBoasVindas);
};


int opcaoUsuario(string mensagemDeBoasVindas)
{
    bool validador = false;
    int opcao = 0;
    while (!validador)
    {
        mensagemDeOpcao(mensagemDeBoasVindas);
        Console.Write("OPÇÃO : ");
        string escolha = Console.ReadLine();
        try
        {
            opcao = int.Parse(escolha);
            if (opcao <= 0 || opcao > 4)
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("Escolha um valor entre 1 e 4 ");
                Console.ResetColor();
            }else{
                validador = true;
            }
        }
        catch
        {
            Console.ForegroundColor = ConsoleColor.Red;
            string mensagem= "Digite um numero para escolha!!";
            Console.WriteLine(mensagem);
            Console.ResetColor();
        }
        
    }
    return  opcao;
}



int opcao = opcaoUsuario(mensagemDeBoasVindas);
Banda teste = new Banda("aa",[12,3243,321]);

switch (opcao)
{
    case 1:
        visualizarBandas();
        break;
    case 2:
        cadastrarBanda();
        break;
    case 3:
        cadastrarMusica();
        break;
    case 4:
        avaliarBanda();
        break;

    default:
        break;
};


void visualizarBandas()
{
    string mensagem = "Exibindo bandas !!";
    ExibirAsteriscos(mensagem);
    Console.WriteLine(mensagem);
    Console.ForegroundColor = ConsoleColor.Blue;
    foreach(var banda in bandas){
        Console.WriteLine(banda);
    }
    Console.ResetColor();
};
void cadastrarBanda()
{

    System.Console.WriteLine("opcao2");

};

void cadastrarMusica()
{
    System.Console.WriteLine("opcao3");

};
void avaliarBanda()
{
    Avaliacao teste = new Avaliacao([2.0f,3.233232f,4.7f,5,6,7,7,]);
    string notas = teste.RecolherNotas();
    Console.WriteLine($"Notas da banda : {notas}");

    teste.VisualizarMedia("BandaAleatoria!");
};