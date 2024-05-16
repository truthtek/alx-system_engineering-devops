file { '/etc/nginx/nginx.conf':
  ensure  => file,
  content => template('nginx/nginx.conf.erb'),
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure => running,
  enable => true,
}

worker_processes auto;
events {
  worker_connections 1024;
}
http {
    sendfile on;
    tcp_nopush on;
    tcp_nodelay on;
    keepalive_timeout 65;
    types_hash_max_size 2048;

    include /etc/nginx/mime.types;
    default_type application/octet-stream;

    # Buffers
    client_body_buffer_size 10K;
    client_header_buffer_size 1k;
    large_client_header_buffers 4 32k;

    # Timeouts
    client_body_timeout 12;
    client_header_timeout 12;
    send_timeout 10;
}
http {
    gzip on;
    gzip_disable "msie6";
    gzip_vary on;
    gzip_proxied any;
    gzip_comp_level 6;
    gzip_buffers 16 8k;
    gzip_http_version 1.1;
    gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;
}

