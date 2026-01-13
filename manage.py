#!/usr/bin/env python
"""Django'нун административдик иштерин аткаруучу куралы."""
import os
import sys

def main():
    """Административдик тапшырмаларды аткаруучу негизги функция."""
    
    # 1. Жөндөөлөрдү туташтыруу: Долбоордун settings.py файлын таап, ишке киргизет
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecom_project.settings')
    
    try:
        # 2. Django'ну ишке киргизүүгө аракет кылат
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # 3. Эгер Django орнотулбаса же виртуалдык чөйрө күйбөсө, катаны көрсөтөт
        raise ImportError(
            "Django табылган жок. Сиз аны орнотконуңузга жана "
            "виртуалдык чөйрөнү (virtual environment) иштеткенге ишениңизби?"
        ) from exc
        
    # 4. Сиз терминалга жазган команданы (мисалы: runserver) кабыл алып, иштетет
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()