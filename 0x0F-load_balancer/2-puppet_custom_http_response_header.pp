# Install Nginx
package { 'nginx':
  ensure => installed,
}

# Get the hostname of the server
$hostname = inline_epp('<%=  @facts["hostname"] %>')

# Configure the custom HTTP header
file { '/etc/nginx/sites-available/default':
  content => "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    server_name _;
    add_header X-Served-By ${hostname};
    location / {
      root /var/www/html;
      index index.html index.htm;
    }
  }",
  notify  => Service['nginx'],
  require => Package['nginx'],
}

# Ensure Nginx service is running
service { 'nginx':
  ensure => running,
  enable => true,
}
