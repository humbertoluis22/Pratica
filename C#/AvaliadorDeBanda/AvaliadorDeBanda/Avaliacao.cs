using System.Xml;

public class Avaliacao{

    private List<float> notas;

    public Avaliacao(List<float> notas ){
        this.notas = notas;
    }

    public List<float> Notas{
        get{
            return notas;
        }
    } 

    public string RecolherNotas(){
        List<string>  new_list = new List<string>();
        foreach (float nota in Notas){
                string nota_formatada = string.Format("{0:0.00}",nota);
                new_list.Add(nota_formatada);
        }

        string notas = String.Join(" - ",new_list);
        return notas;
    }

    public void AdicionarNota(float nota){
        if(nota > 0 & nota < 10){
            Notas.Add(nota);
        }else{
            Console.ForegroundColor =  ConsoleColor.Red;
            Console.WriteLine("Adicione uma nota valida !!");
            Console.WriteLine("Entre 0.0 e 10.0 ");
            Console.ResetColor();
        }
    }

    public void VisualizarMedia(string nomeBanda){
        float media = Notas.Sum() / Notas.Count;
        string stringMedia = string.Format("{0:0.00}",media);
        stringMedia = stringMedia.Replace(",",".");
        Console.WriteLine($"A banda {nomeBanda} tem a media de {stringMedia} ");
    }

}