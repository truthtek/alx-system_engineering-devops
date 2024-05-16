# Fix nginx error 24: too many open files

exec {'fix'
    provider => shell,
    command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
    before   => Exec['restart nginx']
}

exec {'restart nginx':
    provider => shell,
    command  => 'sudo service nginx restart'
}
