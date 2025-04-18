using Jwt.Service;
using Jwt.Models;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddTransient<TokenService>(); // injeção de dependencia

// Add services to the container.


var app = builder.Build();


app.MapGet("/",(TokenService service) => service.Generate(
    new User(
    1, 
    "Humbertoteste@gmail.com",
    "password123",
    new[]
    {
        "student",
        "Premium"
    }
    )));

app.Run();
