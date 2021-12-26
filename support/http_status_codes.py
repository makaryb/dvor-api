# 1xx: Informational (информационные):

# Continue («продолжай»)
CODE_100_CONTINUE = 100
# Switching Protocols («переключение протоколов»)
CODE_101_SWITCHING_PROTOCOLS = 101
# Processing («идёт обработка»)
CODE_102_PROCESSING = 102
# Early Hints («ранняя метаинформация»)
CODE_103_EARLY_HINTS = 103

# 2xx: Success (успешно):

# OK («хорошо»)
CODE_200_OK = 200
# Created («создано»)
CODE_201_CREATED = 201
# Accepted («принято»)
CODE_202_ACCEPTED = 202
# Non-Authoritative Information («информация не авторитетна»)
CODE_203_NONE_AUTHORITATIVE_INFORMATION = 203
# No Content («нет содержимого»)
CODE_204_NO_CONTENT = 204
# Reset Content («сбросить содержимое»)
CODE_205_RESET_CONTENT = 205
# Partial Content («частичное содержимое»)
CODE_206_PARTIAL_CONTENT = 206
# Multi-Status («многостатусный»)
CODE_207_MULTI_STATUS = 207
# Already Reported («уже сообщалось»)
CODE_208_ALREADY_REPORTED = 208
# IM Used («использовано IM»).
CODE_226_IM_USED = 226

# 3xx: Redirection (перенаправление):

# Multiple Choices («множество выборов»)
CODE_300_MULTIPLE_CHOICES = 300
# Moved Permanently («перемещено навсегда»)
CODE_301_MOVED_PERMANENTLY = 301
# Moved Temporarily («перемещено временно»), 302 Found («найдено»)
CODE_302_MOVED_TEMPORARILY = 302
# See Other («смотреть другое»)
CODE_303_SEE_OTHER = 303
# Not Modified («не изменялось»)
CODE_304_MODIFIED = 304
# Use Proxy («использовать прокси»)
CODE_305_USE_PROXY = 305
# Temporary Redirect («временное перенаправление»)
CODE_307_TEMPORARY_REDIRECT = 307
# Permanent Redirect («постоянное перенаправление»)
CODE_PERMANENT_REDIRECT = 308

# 4xx: Client Error (ошибка клиента):

# Bad Request («неправильный, некорректный запрос»)
CODE_400_BAD_REQUEST = 400
# Unauthorized («не авторизован (не представился)»)
CODE_401_UNAUTHORIZED = 401
# Payment Required («необходима оплата»)
CODE_402_PAYMENT_REQUIRED = 402
# Forbidden («запрещено (не уполномочен)»)
CODE_403_FORBIDDEN = 403
# Not Found («не найдено»)
CODE_404_NOT_FOUND = 404
# Method Not Allowed («метод не поддерживается»)
CODE_405_METHOD_NOT_ALLOWED = 405
# Not Acceptable («неприемлемо»)
CODE_406_NOT_ACCEPTABLE = 406
# Proxy Authentication Required («необходима аутентификация прокси»)
CODE_407_PROXY_AUTHENTICATION_REQUIRED = 407
# Request Timeout («истекло время ожидания»)
CODE_408_REQUEST_TIMEOUT = 408
# Conflict («конфликт»)
CODE_409_CONFLICT = 409
# Gone («удалён»)
CODE_410_GONE = 410
# Length Required («необходима длина»)
CODE_411_LENGTH_REQUIRED = 411
# Precondition Failed («условие ложно»)
CODE_412_PRECONDITION_FAILED = 412
# Payload Too Large («полезная нагрузка слишком велика»)
CODE_413_PAYLOAD_TOO_LARGE = 413
# URI Too Long («URI слишком длинный»)
CODE_414_URL_TOO_LONG = 414
# Unsupported Media Type («неподдерживаемый тип данных»)
CODE_415_UNSUPPORTED_MEDIA_TYPE = 415
# Range Not Satisfiable («диапазон не достижим»)
CODE_416_RANGE_NOT_SPECIFIABLE = 416
# Expectation Failed («ожидание не удалось»)
CODE_417_EXPECTATION_FAILED = 417
# I’m a teapot («я — чайник»)
CODE_418_I_AM_A_TEAPOT = 418
# Authentication Timeout (not in RFC 2616) («обычно ошибка проверки CSRF»)
CODE_419_AUTHENTICATION_TIMEOUT = 419
# Misdirected Request
CODE_421_MISDIRECTED_REQUEST = 421
# Unprocessable Entity («необрабатываемый экземпляр»)
CODE_422_UPROCESSABLE_ENTITY = 422
# Locked («заблокировано»)
CODE_423_LOCKED = 423
# Failed Dependency («невыполненная зависимость»)
CODE_424_FAILED_DEPENDENCY = 424
# Too Early («слишком рано»)
CODE_425_TOO_EARLY = 425
# Upgrade Required («необходимо обновление»)
CODE_426_UPGRADE_REQUIRED = 426
# Precondition Required («необходимо предусловие»)
CODE_428_PRECONDITION_REQUIRED = 428
# Too Many Requests («слишком много запросов»)
CODE_429_TOO_MANY_REQUESTS = 429
# Request Header Fields Too Large («поля заголовка запроса слишком большие»)
CODE_431_REQUEST_HEADER_FIELDS_TOO_LARGE = 431
# Retry With («повторить с»)
CODE_449_RETRY_WITH = 449
# Unavailable For Legal Reasons («недоступно по юридическим причинам»)
CODE_451_UNAVAILABLE_FOR_LEGAL_REASONS = 451
# Client Closed Request (клиент закрыл соединение)
CODE_499_CLIENT_CLOSED_REQUEST = 499

# 5xx: Server Error (ошибка сервера):

# Internal Server Error («внутренняя ошибка сервера»)
CODE_500_INTERNAL_SERVER_ERROR = 500
# Not Implemented («не реализовано»)
CODE_501_NOT_IMPLEMENTED = 501
# Bad Gateway («плохой, ошибочный шлюз»)
CODE_502_BAD_GATEWAY = 502
# Service Unavailable («сервис недоступен»)
CODE_503_SERVICE_UNAVAILABLE = 503
# Gateway Timeout («шлюз не отвечает»)
CODE_504_GATEWAY_TIMEOUT = 504
# HTTP Version Not Supported («версия HTTP не поддерживается»)
CODE_505_HTTP_VERSION_NOT_SUPPORTED = 505
# Variant Also Negotiates («вариант тоже проводит согласование»)
CODE_506_VARIANT_ALSO_NEGOTIATES = 506
# Insufficient Storage («переполнение хранилища»)
CODE_507_INSUFFICIENT_STORAGE = 507
# Loop Detected («обнаружено бесконечное перенаправление»)
CODE_508_LOOP_DETECTED = 508
# Bandwidth Limit Exceeded («исчерпана пропускная ширина канала»);
CODE_509_BANDWIDTH_LIMIT_EXCEEDED = 509
# Not Extended («не расширено»)
CODE_510_NOT_EXTENDED = 510
# Network Authentication Required («требуется сетевая аутентификация»)
CODE_511_NETWORK_AUTHENTICATION_REQUIRED = 511
# Unknown Error («неизвестная ошибка»)
CODE_520_UNKNOWN_ERROR = 520
# Web Server Is Down («веб-сервер не работает»)
CODE_521_WEB_SERVER_IS_DOWN = 521
# Connection Timed Out («соединение не отвечает»)
CODE_522_CONNECTION_TIMED_OUT = 522
# Origin Is Unreachable («источник недоступен»)
CODE_523_ORIGIN_IS_UNREACHABLE = 523
# A Timeout Occurred («время ожидания истекло»)
CODE_524_A_TIMEOUT_OCCURRED = 524
# SSL Handshake Failed («квитирование SSL не удалось»)
CODE_525_HANDSHAKE_FAILED = 525
# Invalid SSL Certificate («недействительный сертификат SSL»)
CODE_526_INVALID_SSL_CERTIFICATE = 526
