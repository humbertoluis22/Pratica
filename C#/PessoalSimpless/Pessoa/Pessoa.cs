public class Pessoa{

    // Campos (ou atributos) privados
    private string nome;
    private int idade; 

    // Construtor da classe
    public Pessoa(string nome,int idade){
        this.nome = nome;
        this.idade = idade;
    }

    // Propriedades 
    public string Nome{
        get {
            return nome;
        }
        set{
            if(value.Length > 0 ){
                nome = value;
            }else{
                Console.WriteLine("Digite um nome valido !!!");
            }
        }
    }

    public int Idade{
        get{
            return idade;
        }
        set{
            if(value > 0  && value < 100 ){
                idade = value;
            }else{
                Console.WriteLine("Idade inválida !!");
            }
        }
    }


    public void ExibirMensagem(){
        Console.WriteLine($"Nome: {nome} || Idade: {idade}");
    }

}