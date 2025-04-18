namespace Jwt.Models
{
    public class User
    {
        public int Id { get; set; }
        public string Email { get; set; }
        public string Password { get; set; }
        public string[] Roles { get; set; }

        public User(int id, string email, string password, string[] roles)
        {
            Id = id;
            Email = email;
            Password = password;
            Roles = roles;
        }
    }
}
