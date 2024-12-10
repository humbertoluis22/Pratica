using System.Diagnostics.Contracts;

public class Banda
{
    private string nome;
    private List<string> musicas;
    
    public Banda(string nome, List<string> musicas ){
        this.nome = nome;
        this.musicas = musicas;
    }

    public string Nome{
        get{
            return nome;
        }
        set{
            if (value != nome){
                nome =value;
            }else{
                Console.WriteLine($"Não foi possivel alterar o nome da banda {nome}");
            }
        }
    }

    public List<string> Musicas{
        get{
            return musicas;
        }
    }

    public void adicionarMusica(string musicas){
        musicas.add() 
    }

}
