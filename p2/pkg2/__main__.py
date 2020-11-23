try:
    from p1 import demo_func
except ImportError:
    def demo_func():
        print("Fell back to p2")

def main():
    demo_func()