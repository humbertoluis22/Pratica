using Microsoft.EntityFrameworkCore;
using PraticaDeConexao.Models;

namespace PraticaDeConexao.Data
{
    public class AppDbContext : DbContext
    {
        public AppDbContext(DbContextOptions<AppDbContext> options) : base(options)
        {
        }

        public DbSet<FuncionarioModel> Funcionarios { get; set; }
        public DbSet<ProdutoModel> Produtos { get; set; }
    }
}
