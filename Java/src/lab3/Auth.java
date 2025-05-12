package lab3;

import java.util.HashMap;
import java.util.Map;

public class Auth {
    private Map<String, User> users;

    public Auth() {
        this.users = new HashMap<>();
        users.put("admin", new User("admin", "admin"));
    }

    public boolean login(String username, String password) {
        User user = users.get(username);
        return user != null && user.getPassword().equals(password);
    }

    public void register(String username, String password) {
        users.put(username, new User(username, password));
    }
}
