// Daybreak Star Map desktop shell. The map itself is the static page in ../app; this crate only
// hosts it in the system webview (WebView2 on Windows) and lets its outbound links open in the
// user's default browser through the opener plugin.

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .plugin(tauri_plugin_opener::init())
        .run(tauri::generate_context!())
        .expect("error while running Daybreak Star Map");
}
