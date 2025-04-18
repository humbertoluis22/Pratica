using Jwt.Models;
using System.IdentityModel.Tokens.Jwt;
using Microsoft.IdentityModel.Tokens;
using System.Text;
using System.Security.Claims;

namespace Jwt.Service
{
    public class TokenService
    {
        public string Generate(User user)
        {
            // cria uma instancia do JwtSecurityTokenHandler
            var handler = new JwtSecurityTokenHandler(); // manipulador

            var key = Encoding.ASCII.GetBytes(Configuration.PrivateKey); // transformar a senha em bits para ser usada em função 

            var credentials = new SigningCredentials(
                new SymmetricSecurityKey(key), // chave para assinatura // espera bits
                SecurityAlgorithms.HmacSha256Signature);// metodo de assinatura

            var tokenDescriptor = new SecurityTokenDescriptor
            {
                Subject = GenerateClaims(user),
                SigningCredentials = credentials,
                Expires = DateTime.UtcNow.AddHours(1),

            }; // o que vai dentro do token


            //gera um token
            var token = handler.CreateToken(tokenDescriptor); // criar um token seguro

            // gera uma string do Token
            var strToken = handler.WriteToken(token); // escrever um string baseado no token anteriormente 

            return strToken;
        }

        // metado para gerar claims // adicionar conteudo ao payload do token
        private static ClaimsIdentity GenerateClaims(User user)
        {
            var ci = new ClaimsIdentity();
            ci.AddClaim(new Claim(ClaimTypes.Name, user.Email));

            foreach(var role in user.Roles)
            {
                ci.AddClaim(new Claim(ClaimTypes.Role, role));
            }
           
            return ci;
        }
    
    }
}
