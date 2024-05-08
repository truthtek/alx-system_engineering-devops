# Fix Apache 500 error issue identified using strace

case $facts['os']['name'] {
  'Ubuntu': {
    $apache_service = 'apache2'
    $apache_config_dir = '/etc/apache2'
  }
  'CentOS', 'RedHat': {
    $apache_service = 'httpd'
    $apache_config_dir = '/etc/httpd'
  }
  default: {
    fail("Unsupported OS ${facts['os']['name']}")
  }
}

# Ensure Apache is running
service { $apache_service:
  ensure => running,
  enable => true,
}

# Fix the issue identified using strace
# Example: Modify Apache configuration file
file { "${apache_config_dir}/conf.d/custom.conf":
  ensure  => file,
  content => "# Custom configuration to fix 500 error\n...",
  notify  => Service[$apache_service],
}
