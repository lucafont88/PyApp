import keyboard

def key_pressed_generator(key_pressed: list):
    print("Tasti premuti:")
    for k in key_pressed:
        print(k)
        yield k

def generate_events():
    while True:
        k = keyboard.read_key()
        print(k)
        yield keyboard.read_key()

key_pressed = []
keyboard.on_release(lambda k: key_pressed.append(k))

print("listening...")

result = keyboard.get_typed_strings(generate_events(), allow_backspace=True)

keyboard.wait('esc')
print("stop listening")

print("Parsed strings:")
#print("DIR strings:")
# print (result)
# val = next(result)
# print(val)
while True:
        s = next(result)
        print(str(s))


print("End")