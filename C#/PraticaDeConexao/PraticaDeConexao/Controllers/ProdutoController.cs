using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using PraticaDeConexao.Data;
using PraticaDeConexao.Models;

namespace PraticaDeConexao.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class ProdutoController : ControllerBase
    {
        private readonly AppDbContext _context;
        public ProdutoController( AppDbContext context)
        {
            _context = context;
        }

        [HttpGet("Produtos")]
        public async Task<List<ProdutoModel>> RecolherProdutos()
        {
            var produtos = await _context.Produtos.ToListAsync();
            return produtos;
        }
    }
}
