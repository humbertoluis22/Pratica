﻿using ConexaoCodeFirst.Models;
using Microsoft.EntityFrameworkCore;
using Microsoft.Identity.Client;

namespace ConexaoCodeFirst.Data
{
    public class AppDbContext : DbContext
    {
        public AppDbContext(DbContextOptions<AppDbContext> options):base(options)
        {
        }

        public DbSet<ProdutoModel> Produtos { get; set; }
        public DbSet<User> Usuarios { get; set; }



    }
}
