using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using PraticaDeConexao.Data;
using PraticaDeConexao.Models;

namespace PraticaDeConexao.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class FuncionarioController : ControllerBase
    {
        private readonly AppDbContext _context;
        public FuncionarioController(AppDbContext context)
        {
            _context = context;
        }

        [HttpGet("Funcionario")]
        public async Task<List<FuncionarioModel>> RecolherFuncionarios()
        {
            var funcionarios = await _context.Funcionarios.ToListAsync();
            return funcionarios;
        }
    }
}
