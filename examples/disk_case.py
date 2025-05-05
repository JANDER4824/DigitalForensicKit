"""
Ejemplo de análisis de imagen de disco con DigitalForensicKit.
"""

from modules.disk_inspector import DiskInspector

def main():
    image_path = "examples/disk.img"
    inspector = DiskInspector(image_path)
    print("Archivos raíz:", inspector.list_files("/"))
    print("Archivos eliminados:", inspector.recover_deleted_files())

if __name__ == "__main__":
    main()