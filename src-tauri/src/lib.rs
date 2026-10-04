// Daybreak Star Map desktop shell. The map itself is the static page in ../app; this crate only
// hosts it in the system webview (WebView2 on Windows), lets its outbound links open in the user's
// default browser through the opener plugin, and gives the page the file dialogs and file access its
// scenarios need (dialog and fs plugins). persisted-scope remembers folders and files the user picked
// in a dialog across launches; it has to be registered after fs.

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .plugin(tauri_plugin_opener::init())
        .plugin(tauri_plugin_fs::init())
        .plugin(tauri_plugin_dialog::init())
        .plugin(tauri_plugin_persisted_scope::init())
        .run(tauri::generate_context!())
        .expect("error while running Daybreak Star Map");
}
