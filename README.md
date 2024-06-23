<p align="center">
  <img src="https://static.wixstatic.com/media/4c5231_3a985f0dcdd34e4d9857b44860614f51~mv2.gif" alt="Recycling Animation">
</p>

# Let's Recycle App

Let's Recycle! — это оконное приложение, предоставляющее информацию о переработке отходов, включая данные о пунктах переработки в Приморском крае. Кроме того, пользователи могут вызвать эко-такси на дом. Проект разработан с использованием Python, SQLite3 и PyQt6. Его цель — повысить осведомленность о защите окружающей среды и облегчить процесс переработки для местного сообщества.

## Установка и локальный запуск

<ol>
  <li>Откройте терминал и склонируйте репозиторий:
    <pre><code>git clone https://github.com/t-anastasiia/Lets-recycle.git</code></pre>
  </li>
  <li>Перейдите в папку со скопированным репозиторием:
    <pre><code>cd Lets-recycle/app</code></pre>
  </li>
  <li>Запустите приложение:
    <pre><code>python main.py</code></pre>
  </li>
</ol>

## Архитектура и используемые паттерны

Проект следует архитектуре MVVM (Model-View-ViewModel) и старается придерживаться принципов SOLID, KISS и DRY.

### Принципы SOLID

<ul>
  <li><b>Single Responsibility Principle</b> (Принцип единственной ответственности): Каждый класс в проекте отвечает за свою отдельную функциональность.</li>
  <li><b>Open/Closed Principle</b> (Принцип открытости/закрытости): Система спроектирована так, чтобы новые функциональности можно было добавлять без изменения существующего кода.</li>
  <li><b>Liskov Substitution Principle</b> (Принцип подстановки Барбары Лисков): Наследующие классы могут замещать базовые классы без изменения их поведения.</li>
  <li><b>Interface Segregation Principle</b> (Принцип разделения интерфейса): Применяются узкие интерфейсы, специфичные для клиентов.</li>
  <li><b>Dependency Inversion Principle</b> (Принцип инверсии зависимостей): Модули верхнего уровня не зависят от модулей нижнего уровня, оба зависят от абстракций.</li>
</ul>

### Принцип KISS

Простота реализации кода (Keep It Simple, Stupid) обеспечивает его легкость для понимания и поддержки.

### Принцип DRY

Принцип "Don't Repeat Yourself" применяется, чтобы избежать дублирования кода и улучшить его поддерживаемость.

### Архитектура MVVM

<ul>
  <li><b>Model</b>: Управляет данными и бизнес-логикой.</li>
  <li><b>View</b>: Определяет структуру и внешний вид пользовательского интерфейса.</li>
  <li><b>ViewModel</b>: Посредник между Model и View, управляет состоянием View и обработкой событий.</li>
</ul>

Проект был спроектирован с учетом бизнес-логики для управления запросами на утилизацию отходов.

## Работа с базами данных

Проект использует SQLite для хранения данных. Взаимодействие с базой данных осуществляется с помощью стандартных библиотек Python для выполнения CRUD операций.

<img src="https://github.com/t-anastasiia/Lets-recycle/assets/121961781/0e947444-51a5-45f8-ba99-9ac523d631e1" alt="Database Schema">

## Скриншоты

### Главное меню
<img src="path_to_main_menu_screenshot" alt="Main Menu">

### Окно запросов
<img src="path_to_requests_window_screenshot" alt="Requests Window">
