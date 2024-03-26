# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Configure Nginx to return "Hello World!"
file { '/var/www/html/index.nginx-debian.html':
  ensure  => present,
  content => "Hello World!\n",
  require => Package['nginx'],
}

# Configure Nginx for redirection
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => @("EOF"/)
    server {
        listen 80;
        server_name _;

        location / {
            root /var/www/html;
            index index.nginx-debian.html;
        }

        location /redirect_me {
            return 301 https://www.example.com;
        }
    }
    | EOF
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Enable the new Nginx configuration
file { '/etc/nginx/sites-enabled/default':
  ensure  => link,
  target  => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
  notify  => Service['nginx'],
}

# Ensure Nginx service is running
service { 'nginx':
  ensure => running,
  enable => true,
}
