# Puppet manifest to install Flask version 2.1.0 using pip3

# Explanation: This manifest installs Flask version 2.1.0 using pip3.

# Ensure the package is installed
package { 'python3-pip':
  ensure => installed,
}

# Install Flask version 2.1.0 using pip3
exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  path    => ['/usr/bin'],
  unless  => '/usr/bin/flask --version | grep "Flask 2.1.0"',
}

