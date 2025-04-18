using Microsoft.IdentityModel.Tokens;
using System.IdentityModel.Tokens.Jwt;
using System.Text;

namespace ConexaoCodeFirst.Service
{
    public class TokenService
    {

        public string GerarToken() { 
            var handler  = new JwtSecurityTokenHandler();

            var key = Encoding.ASCII.GetBytes(Configuration.PrivateKey);

            var credentials = new SigningCredentials
             (
                new SymmetricSecurityKey(key),
                SecurityAlgorithms.HmacSha256Signature
             );

            var tokenDescriptor = new SecurityTokenDescriptor(
                Subject = GenerateClaims(user),
                SigningCredentials = credentials,
                Expires = DateTime.UtcNow.AddHours(3)
                );
            var token = handler.CreateToken(tokenDescriptor);

            var strToken = handler.WriteToken(token);

            return strToken;

        }
    }
}
