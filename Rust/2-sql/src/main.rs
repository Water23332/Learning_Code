use rusqlite::{Connection, Result as SqlResult};
use std::env;
use std::time::Instant;

fn main() -> SqlResult<()> {
    let start = Instant::now();
    
    let args: Vec<String> = env::args().collect();
    
    if args.len() != 2 {
        println!("Usage: {} <kanji>", args[0]);
        return Ok(());
    }

    let kanji = &args[1];
    let conn = Connection::open("db/japanese_dict.db")?;
    
    // Speed optimizations using pragma_update
    conn.pragma_update(None, "journal_mode", "WAL")?;
    conn.pragma_update(None, "synchronous", "NORMAL")?;
    conn.pragma_update(None, "cache_size", 1000000i64)?;
    conn.pragma_update(None, "temp_store", "MEMORY")?;
    conn.pragma_update(None, "mmap_size", 30000000000i64)?;

    let mut stmt = conn.prepare_cached("SELECT definition FROM dict WHERE kanji = ?")?;
    let definition_iter = stmt.query_map([kanji], |row| row.get::<_, String>(0))?;

    let mut found = false;
    for definition in definition_iter {
        found = true;
        println!("{}", definition?);
    }

    if !found {
        eprintln!("No definition found for '{}'", kanji);
    }

    let duration = start.elapsed();
    eprintln!("Time elapsed: {:.2} ms", duration.as_secs_f64() * 1000.0);

    Ok(())
}
