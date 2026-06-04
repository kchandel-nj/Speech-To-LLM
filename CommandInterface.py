class Command:

    def __init__(self):
        pass

    def interpret_command(self, cmd: str):
        """
        Interprets a command supplied by the AI.

        Args:
            cmd (str): The command that the AI provided.
        """

        match cmd[0 : cmd.index(" ")]:
            case "1":
                print(f"Turn on: {cmd[cmd.index(" ") + 1]}")
                # Call a method
            case "2":
                print(f"Turn off: {cmd[cmd.index(" ") + 1]}")
                # Call a method
            case _:
                print("Unknown command")