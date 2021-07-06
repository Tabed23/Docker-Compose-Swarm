FROM php:7.1.2-apache



RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \\
    HASH="$(wget -q -O - https://composer.github.io/installer.sig)" && \\
    php -r "if (hash_file('SHA384', 'composer-setup.php') === '$HASH') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" && \\
    php composer-setup.php --install-dir=/usr/local/bin --filename=composer && \\
    mv composer.phar /usr/local/bin/composer

COPY ./composer.json /var/www/html

RUN apt-get update && apt-get install -y git

RUN composer install

RUN sed -i 's/DocumentRoot.*s/DocumentRoot \/var\/www\/html\/public' /etc/apache2/sites-enabled/000-default.conf

RUN a2enmoe rewrite