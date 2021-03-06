import logging
from flask import Flask, abort


app = Flask(__name__)


@app.route('/user/register', methods=['POST'])
def register_user():
    """Register a new user.
    The payload must be a JSON of the form
    {
        'name': name,
        'email': email
    }
    A confirmation token for the action REGISTER must be created, stored and sent as part of the response

    :return:
        - 201 (Created) + empty response + sends a mail with a token
        - 400 (Bad Request) if the email address is not valid
        - 409 (Conflict) if the email is already in use + an error message saying so
        - 424 (Method Failure) if the email address is not valid or we couldn't send the mail
    """
    abort(501, 'User features still not available')


@app.route('/user/delete', methods=['DELETE'])
def delete_user():
    """Delete an existing user plus all his game entries.
    The payload must be a JSON with ONLY one of these
    {
        'email': email,
        'token': token
    }
    If email is defined then a confirmation link will be sent
    If a valid token is provided then user deletion happens immediately

    :return:
        - 200 (OK) + confirmation message if user was successfully deleted
        - 400 (Bad Request) if both token and email address are specified, or if any of those are not valid
        - 424 (Method Failure) if we couldn't send the mail
    """
    abort(501, 'User features still not available')


@app.route('/user/confirm/<string:token>', methods=['POST'])
def confirm_user(token):
    """Confirm a user registration/deletion action
    :param token: Confirmation token
    :return:
        - 201 (Created) if token maps to a registration action + a JSON {'player_token': player_token}
        - 200 (OK) if token maps to a deletion action
        - 400 (Bad Request) if the token is not valid
    """
    abort(501, 'User features still not available')


@app.route('/user/recover_token/<string:email>', methods=['GET'])
def recover_token(email):
    """Send the player token corresponding to the given email (if any)
    :param email: email address
    :return:
        - 400 (Bad Request) if the mail address is not valid (wrong mail syntax)
        - 200 (OK) otherwise regardless of the mail address actually existing or not
    """
    abort(501, 'User features still not available')


@app.route('/user/game/<string:game_id>', methods=['GET'])
def get_game(game_id):
    """Return a JSON with the specified game
    :param game_id: Game id
      {
        'id': id,
        'word_length': int,
        'max_guesses': int,
        'actions': [Action {'guess': guess, 'answer':answer}]}
      }
    """
    pass


@app.route('/user/games/<string:player_token>', methods=['GET'])
def get_game_history(player_token):
    """Return the whole game history for a player
    :param player_token: Player token
    :return:
        - 400 (Bad Request) if player token is not valid
        - 200 (OK) with a JSON
          {
            'games':[game1, game2, ..., gamen],
            'status': ['win', 'defeat', 'ongoing']
          }
          with game_i being a JSON as specified in /user/game/<game_id:str> GET
          If won is true then it means that the last guess was correct
    """
    pass


@app.route('/user/game/stats/<string:player_token>', methods=['GET'])
def get_user_game_stats(player_token):
    """Return some stats for the given game
    :param player_token: Player token
    :return:
        - 400 (Bad Request) if player token is not valid
        - 200 (OK) with a JSON TBD
    """
    pass


@app.route('/game/list_word_lists', methods=['GET'])
def list_word_lists():
    """List the available word lists to play the game
    :return:
        - 200 (OK) + JSON with a list containing the names of the available word lists
    """
    pass


@app.route('/game/start/<string:player_token>', methods=['POST'])
def start_new_game(player_token):
    """Start a new game, payload must be a JSON
    {
        'word_list': int,
        'max_guesses': int
    }
    word_list must be one of the word lists returned in list_word_lists
    :param player_token: Player token
    :return:
        - 400 (Bad Request) if player_token or word_length are not valid
        - 201 (Created) + a JSON with the new game id
    """
    pass


@app.route('/game/play/<string:player_token>/<string:game_id>', methods=['PUT'])
def play_game(player_token, game_id):
    """Play a turn in the player's current game, payload must be a JSON
    {
        'guess': guess
    }
    :param player_token: Player token
    :param game_id: Game id
    :return:
        - 400 (Bad Request) if player_token does not exist or there is no game with the given id for this player
        - 422 (Unprocessable Entity) if the guessed word is not correct (wrong length, word doesnt exist, etc)
        - 200 (OK) if the guess is correct + JSON with a list of colors
    """
    pass


@app.route('/game/stop/<string:player_token>/<string:game_id>', methods=['DELETE'])
def delete_game(player_token, game_id):
    """Delete a game for a given user
    :param player_token: Player token
    :param game_id: Game id
    :return:
        - 400 (Bad Request) if player_token does not exist or there is no game with the given id for this player
        - 200 (OK) if managed to correctly delete the game
    """
    pass
